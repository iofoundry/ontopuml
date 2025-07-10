package gov.nist;

import java.io.File;
import java.util.Set;
import java.util.stream.Collectors;

import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLClass;
import org.semanticweb.owlapi.model.OWLClassExpression;
import org.semanticweb.owlapi.model.OWLDataAllValuesFrom;
import org.semanticweb.owlapi.model.OWLDataFactory;
import org.semanticweb.owlapi.model.OWLDataIntersectionOf;
import org.semanticweb.owlapi.model.OWLDataProperty;
import org.semanticweb.owlapi.model.OWLDataRange;
import org.semanticweb.owlapi.model.OWLDatatypeRestriction;
import org.semanticweb.owlapi.model.OWLEquivalentClassesAxiom;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.model.OWLOntologyCreationException;
import org.semanticweb.owlapi.model.OWLOntologyManager;
import org.semanticweb.owlapi.util.AutoIRIMapper;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) throws OWLOntologyCreationException
    {
        System.out.println( "Hello World!" );
        OWLOntologyManager manager = OWLManager.createOWLOntologyManager();
        File file = new File("C:\\Users\\ans83\\git\\ontopuml\\nowl\\src\\main\\resources\\benchmark-simple-modified.rdf"); // Replace with your file path
        
        File importsFolder = new File("C:\\Users\\ans83\\git\\ontopuml\\nowl\\src\\main\\resources");
        AutoIRIMapper mapper = new AutoIRIMapper(importsFolder, true);
        manager.addIRIMapper(mapper);
        
        OWLOntology ontology = manager.loadOntologyFromOntologyDocument(file);
        
        
        
        // Get all classes from the ontology
        Set<OWLClass> classes = ontology.classesInSignature().collect(Collectors.toSet());

        // Print the classes
        System.out.println("Classes in the ontology:");
        IRI classIRI = IRI.create("http://nist.gov/nowl/benchmark-simple/DataAllComplexDatatypeClass");
        OWLDataFactory factory = manager.getOWLDataFactory();
        OWLClass targetClass = factory.getOWLClass(classIRI);

        for (OWLEquivalentClassesAxiom axiom : ontology.getEquivalentClassesAxioms(targetClass)) {
            for (OWLClassExpression expr : axiom.getClassExpressionsMinus(targetClass)) {
                if (expr instanceof OWLDataAllValuesFrom) {
                    OWLDataAllValuesFrom restriction = (OWLDataAllValuesFrom) expr;
                    OWLDataProperty property = restriction.getProperty().asOWLDataProperty();
                    OWLDataRange dataRange = restriction.getFiller();

                    System.out.println("Property: " + property);
                    System.out.println("data range: " + dataRange);

                    // If it's an intersection
                    if (dataRange instanceof OWLDataIntersectionOf) {
                        for (OWLDataRange conjunct : ((OWLDataIntersectionOf) dataRange).getOperands()) {
                            System.out.println(" - Conjunct: " + conjunct);
                            if(conjunct instanceof OWLDatatypeRestriction){
                                ((OWLDatatypeRestriction)conjunct).facetRestrictions().forEach(r->System.out.println(r)); 
                            }
                        }
                    }
                }
            }
        }
    }
}
