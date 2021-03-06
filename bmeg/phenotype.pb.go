// Code generated by protoc-gen-go.
// source: phenotype.proto
// DO NOT EDIT!

package bmeg

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

type ResponseSummary_SummaryType int32

const (
	ResponseSummary_UNKNOWN       ResponseSummary_SummaryType = 0
	ResponseSummary_EC50          ResponseSummary_SummaryType = 1
	ResponseSummary_IC50          ResponseSummary_SummaryType = 2
	ResponseSummary_LD50          ResponseSummary_SummaryType = 3
	ResponseSummary_GR50          ResponseSummary_SummaryType = 4
	ResponseSummary_AMAX          ResponseSummary_SummaryType = 5
	ResponseSummary_AUC           ResponseSummary_SummaryType = 6
	ResponseSummary_ACTIVITY_AREA ResponseSummary_SummaryType = 7
	ResponseSummary_RMSE          ResponseSummary_SummaryType = 8
)

var ResponseSummary_SummaryType_name = map[int32]string{
	0: "UNKNOWN",
	1: "EC50",
	2: "IC50",
	3: "LD50",
	4: "GR50",
	5: "AMAX",
	6: "AUC",
	7: "ACTIVITY_AREA",
	8: "RMSE",
}
var ResponseSummary_SummaryType_value = map[string]int32{
	"UNKNOWN":       0,
	"EC50":          1,
	"IC50":          2,
	"LD50":          3,
	"GR50":          4,
	"AMAX":          5,
	"AUC":           6,
	"ACTIVITY_AREA": 7,
	"RMSE":          8,
}

func (x ResponseSummary_SummaryType) String() string {
	return proto.EnumName(ResponseSummary_SummaryType_name, int32(x))
}
func (ResponseSummary_SummaryType) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor6, []int{6, 0}
}

type ResponseCurve_ResponseType int32

const (
	ResponseCurve_UNKNOWN  ResponseCurve_ResponseType = 0
	ResponseCurve_GROWTH   ResponseCurve_ResponseType = 1
	ResponseCurve_ACTIVITY ResponseCurve_ResponseType = 2
)

var ResponseCurve_ResponseType_name = map[int32]string{
	0: "UNKNOWN",
	1: "GROWTH",
	2: "ACTIVITY",
}
var ResponseCurve_ResponseType_value = map[string]int32{
	"UNKNOWN":  0,
	"GROWTH":   1,
	"ACTIVITY": 2,
}

func (x ResponseCurve_ResponseType) String() string {
	return proto.EnumName(ResponseCurve_ResponseType_name, int32(x))
}
func (ResponseCurve_ResponseType) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor6, []int{7, 0}
}

type PhenotypeAssociation struct {
	Id   string `protobuf:"bytes,1,opt,name=id" json:"id,omitempty"`
	Gid  string `protobuf:"bytes,2,opt,name=gid" json:"gid,omitempty"`
	Type string `protobuf:"bytes,3,opt,name=type" json:"type,omitempty"`
	// Target: VariantCall Biosample Individual Gene
	HasGenotype []string `protobuf:"bytes,4,rep,name=hasGenotype" json:"hasGenotype,omitempty"`
	// Target: Phenotype
	HasPhenotype []string `protobuf:"bytes,5,rep,name=hasPhenotype" json:"hasPhenotype,omitempty"`
	// The context is unique to the PhenotypeAssociation. Could involve Drug or Evidence.
	// Target: Drug Evidence
	HasContext []string `protobuf:"bytes,6,rep,name=hasContext" json:"hasContext,omitempty"`
}

func (m *PhenotypeAssociation) Reset()                    { *m = PhenotypeAssociation{} }
func (m *PhenotypeAssociation) String() string            { return proto.CompactTextString(m) }
func (*PhenotypeAssociation) ProtoMessage()               {}
func (*PhenotypeAssociation) Descriptor() ([]byte, []int) { return fileDescriptor6, []int{0} }

func (m *PhenotypeAssociation) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *PhenotypeAssociation) GetGid() string {
	if m != nil {
		return m.Gid
	}
	return ""
}

func (m *PhenotypeAssociation) GetType() string {
	if m != nil {
		return m.Type
	}
	return ""
}

func (m *PhenotypeAssociation) GetHasGenotype() []string {
	if m != nil {
		return m.HasGenotype
	}
	return nil
}

func (m *PhenotypeAssociation) GetHasPhenotype() []string {
	if m != nil {
		return m.HasPhenotype
	}
	return nil
}

func (m *PhenotypeAssociation) GetHasContext() []string {
	if m != nil {
		return m.HasContext
	}
	return nil
}

type Phenotype struct {
	Id          string   `protobuf:"bytes,1,opt,name=id" json:"id,omitempty"`
	Gid         string   `protobuf:"bytes,2,opt,name=gid" json:"gid,omitempty"`
	Type        string   `protobuf:"bytes,3,opt,name=type" json:"type,omitempty"`
	IsType      []string `protobuf:"bytes,4,rep,name=isType" json:"isType,omitempty"`
	Description string   `protobuf:"bytes,5,opt,name=description" json:"description,omitempty"`
}

func (m *Phenotype) Reset()                    { *m = Phenotype{} }
func (m *Phenotype) String() string            { return proto.CompactTextString(m) }
func (*Phenotype) ProtoMessage()               {}
func (*Phenotype) Descriptor() ([]byte, []int) { return fileDescriptor6, []int{1} }

func (m *Phenotype) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *Phenotype) GetGid() string {
	if m != nil {
		return m.Gid
	}
	return ""
}

func (m *Phenotype) GetType() string {
	if m != nil {
		return m.Type
	}
	return ""
}

func (m *Phenotype) GetIsType() []string {
	if m != nil {
		return m.IsType
	}
	return nil
}

func (m *Phenotype) GetDescription() string {
	if m != nil {
		return m.Description
	}
	return ""
}

type GeneOntologyTerm struct {
	Id         string   `protobuf:"bytes,1,opt,name=id" json:"id,omitempty"`
	Namespace  string   `protobuf:"bytes,2,opt,name=namespace" json:"namespace,omitempty"`
	Def        string   `protobuf:"bytes,3,opt,name=def" json:"def,omitempty"`
	Comment    string   `protobuf:"bytes,4,opt,name=comment" json:"comment,omitempty"`
	Synonym    string   `protobuf:"bytes,5,opt,name=synonym" json:"synonym,omitempty"`
	IsA        []string `protobuf:"bytes,6,rep,name=is_a" json:"is_a,omitempty"`
	AltId      []string `protobuf:"bytes,7,rep,name=alt_id" json:"alt_id,omitempty"`
	Subset     []string `protobuf:"bytes,8,rep,name=subset" json:"subset,omitempty"`
	Xref       []string `protobuf:"bytes,9,rep,name=xref" json:"xref,omitempty"`
	IsObsolete bool     `protobuf:"varint,10,opt,name=is_obsolete" json:"is_obsolete,omitempty"`
	Consider   []string `protobuf:"bytes,11,rep,name=consider" json:"consider,omitempty"`
}

func (m *GeneOntologyTerm) Reset()                    { *m = GeneOntologyTerm{} }
func (m *GeneOntologyTerm) String() string            { return proto.CompactTextString(m) }
func (*GeneOntologyTerm) ProtoMessage()               {}
func (*GeneOntologyTerm) Descriptor() ([]byte, []int) { return fileDescriptor6, []int{2} }

func (m *GeneOntologyTerm) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *GeneOntologyTerm) GetNamespace() string {
	if m != nil {
		return m.Namespace
	}
	return ""
}

func (m *GeneOntologyTerm) GetDef() string {
	if m != nil {
		return m.Def
	}
	return ""
}

func (m *GeneOntologyTerm) GetComment() string {
	if m != nil {
		return m.Comment
	}
	return ""
}

func (m *GeneOntologyTerm) GetSynonym() string {
	if m != nil {
		return m.Synonym
	}
	return ""
}

func (m *GeneOntologyTerm) GetIsA() []string {
	if m != nil {
		return m.IsA
	}
	return nil
}

func (m *GeneOntologyTerm) GetAltId() []string {
	if m != nil {
		return m.AltId
	}
	return nil
}

func (m *GeneOntologyTerm) GetSubset() []string {
	if m != nil {
		return m.Subset
	}
	return nil
}

func (m *GeneOntologyTerm) GetXref() []string {
	if m != nil {
		return m.Xref
	}
	return nil
}

func (m *GeneOntologyTerm) GetIsObsolete() bool {
	if m != nil {
		return m.IsObsolete
	}
	return false
}

func (m *GeneOntologyTerm) GetConsider() []string {
	if m != nil {
		return m.Consider
	}
	return nil
}

type Evidence struct {
	Id   string `protobuf:"bytes,1,opt,name=id" json:"id,omitempty"`
	Gid  string `protobuf:"bytes,2,opt,name=gid" json:"gid,omitempty"`
	Type string `protobuf:"bytes,3,opt,name=type" json:"type,omitempty"`
	// In the future, we might want to turn this field into an edge to a full-fledged Publication object
	Pmid []string `protobuf:"bytes,4,rep,name=pmid" json:"pmid,omitempty"`
	// Information about this evidence item
	Info map[string]string `protobuf:"bytes,5,rep,name=info" json:"info,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
}

func (m *Evidence) Reset()                    { *m = Evidence{} }
func (m *Evidence) String() string            { return proto.CompactTextString(m) }
func (*Evidence) ProtoMessage()               {}
func (*Evidence) Descriptor() ([]byte, []int) { return fileDescriptor6, []int{3} }

func (m *Evidence) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *Evidence) GetGid() string {
	if m != nil {
		return m.Gid
	}
	return ""
}

func (m *Evidence) GetType() string {
	if m != nil {
		return m.Type
	}
	return ""
}

func (m *Evidence) GetPmid() []string {
	if m != nil {
		return m.Pmid
	}
	return nil
}

func (m *Evidence) GetInfo() map[string]string {
	if m != nil {
		return m.Info
	}
	return nil
}

type Compound struct {
	Id        string `protobuf:"bytes,1,opt,name=id" json:"id,omitempty"`
	Gid       string `protobuf:"bytes,2,opt,name=gid" json:"gid,omitempty"`
	Type      string `protobuf:"bytes,3,opt,name=type" json:"type,omitempty"`
	Name      string `protobuf:"bytes,4,opt,name=name" json:"name,omitempty"`
	Smiles    string `protobuf:"bytes,9,opt,name=smiles" json:"smiles,omitempty"`
	Target    string `protobuf:"bytes,5,opt,name=target" json:"target,omitempty"`
	Report    string `protobuf:"bytes,6,opt,name=report" json:"report,omitempty"`
	Status    string `protobuf:"bytes,7,opt,name=status" json:"status,omitempty"`
	Rationale string `protobuf:"bytes,8,opt,name=rationale" json:"rationale,omitempty"`
	// Each synonym may end up as a node.
	Synonyms []string          `protobuf:"bytes,10,rep,name=synonyms" json:"synonyms,omitempty"`
	Info     map[string]string `protobuf:"bytes,11,rep,name=info" json:"info,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
}

func (m *Compound) Reset()                    { *m = Compound{} }
func (m *Compound) String() string            { return proto.CompactTextString(m) }
func (*Compound) ProtoMessage()               {}
func (*Compound) Descriptor() ([]byte, []int) { return fileDescriptor6, []int{4} }

func (m *Compound) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *Compound) GetGid() string {
	if m != nil {
		return m.Gid
	}
	return ""
}

func (m *Compound) GetType() string {
	if m != nil {
		return m.Type
	}
	return ""
}

func (m *Compound) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

func (m *Compound) GetSmiles() string {
	if m != nil {
		return m.Smiles
	}
	return ""
}

func (m *Compound) GetTarget() string {
	if m != nil {
		return m.Target
	}
	return ""
}

func (m *Compound) GetReport() string {
	if m != nil {
		return m.Report
	}
	return ""
}

func (m *Compound) GetStatus() string {
	if m != nil {
		return m.Status
	}
	return ""
}

func (m *Compound) GetRationale() string {
	if m != nil {
		return m.Rationale
	}
	return ""
}

func (m *Compound) GetSynonyms() []string {
	if m != nil {
		return m.Synonyms
	}
	return nil
}

func (m *Compound) GetInfo() map[string]string {
	if m != nil {
		return m.Info
	}
	return nil
}

type DoseResponse struct {
	Dose     float64 `protobuf:"fixed64,1,opt,name=dose" json:"dose,omitempty"`
	Response float64 `protobuf:"fixed64,2,opt,name=response" json:"response,omitempty"`
}

func (m *DoseResponse) Reset()                    { *m = DoseResponse{} }
func (m *DoseResponse) String() string            { return proto.CompactTextString(m) }
func (*DoseResponse) ProtoMessage()               {}
func (*DoseResponse) Descriptor() ([]byte, []int) { return fileDescriptor6, []int{5} }

func (m *DoseResponse) GetDose() float64 {
	if m != nil {
		return m.Dose
	}
	return 0
}

func (m *DoseResponse) GetResponse() float64 {
	if m != nil {
		return m.Response
	}
	return 0
}

type ResponseSummary struct {
	Type  ResponseSummary_SummaryType `protobuf:"varint,1,opt,name=type,enum=bmeg.ResponseSummary_SummaryType" json:"type,omitempty"`
	Value float64                     `protobuf:"fixed64,2,opt,name=value" json:"value,omitempty"`
	Unit  string                      `protobuf:"bytes,3,opt,name=unit" json:"unit,omitempty"`
}

func (m *ResponseSummary) Reset()                    { *m = ResponseSummary{} }
func (m *ResponseSummary) String() string            { return proto.CompactTextString(m) }
func (*ResponseSummary) ProtoMessage()               {}
func (*ResponseSummary) Descriptor() ([]byte, []int) { return fileDescriptor6, []int{6} }

func (m *ResponseSummary) GetType() ResponseSummary_SummaryType {
	if m != nil {
		return m.Type
	}
	return ResponseSummary_UNKNOWN
}

func (m *ResponseSummary) GetValue() float64 {
	if m != nil {
		return m.Value
	}
	return 0
}

func (m *ResponseSummary) GetUnit() string {
	if m != nil {
		return m.Unit
	}
	return ""
}

type ResponseCurve struct {
	Gid            string                     `protobuf:"bytes,1,opt,name=gid" json:"gid,omitempty"`
	ResponseType   ResponseCurve_ResponseType `protobuf:"varint,2,opt,name=responseType,enum=bmeg.ResponseCurve_ResponseType" json:"responseType,omitempty"`
	Values         []*DoseResponse            `protobuf:"bytes,3,rep,name=values" json:"values,omitempty"`
	GrowthStandard float64                    `protobuf:"fixed64,4,opt,name=growthStandard" json:"growthStandard,omitempty"`
	Compound       string                     `protobuf:"bytes,5,opt,name=compound" json:"compound,omitempty"`
	Sample         string                     `protobuf:"bytes,6,opt,name=sample" json:"sample,omitempty"`
	Summary        []*ResponseSummary         `protobuf:"bytes,7,rep,name=summary" json:"summary,omitempty"`
	Controls       []float64                  `protobuf:"fixed64,8,rep,packed,name=controls" json:"controls,omitempty"`
	Blanks         []float64                  `protobuf:"fixed64,9,rep,packed,name=blanks" json:"blanks,omitempty"`
}

func (m *ResponseCurve) Reset()                    { *m = ResponseCurve{} }
func (m *ResponseCurve) String() string            { return proto.CompactTextString(m) }
func (*ResponseCurve) ProtoMessage()               {}
func (*ResponseCurve) Descriptor() ([]byte, []int) { return fileDescriptor6, []int{7} }

func (m *ResponseCurve) GetGid() string {
	if m != nil {
		return m.Gid
	}
	return ""
}

func (m *ResponseCurve) GetResponseType() ResponseCurve_ResponseType {
	if m != nil {
		return m.ResponseType
	}
	return ResponseCurve_UNKNOWN
}

func (m *ResponseCurve) GetValues() []*DoseResponse {
	if m != nil {
		return m.Values
	}
	return nil
}

func (m *ResponseCurve) GetGrowthStandard() float64 {
	if m != nil {
		return m.GrowthStandard
	}
	return 0
}

func (m *ResponseCurve) GetCompound() string {
	if m != nil {
		return m.Compound
	}
	return ""
}

func (m *ResponseCurve) GetSample() string {
	if m != nil {
		return m.Sample
	}
	return ""
}

func (m *ResponseCurve) GetSummary() []*ResponseSummary {
	if m != nil {
		return m.Summary
	}
	return nil
}

func (m *ResponseCurve) GetControls() []float64 {
	if m != nil {
		return m.Controls
	}
	return nil
}

func (m *ResponseCurve) GetBlanks() []float64 {
	if m != nil {
		return m.Blanks
	}
	return nil
}

func init() {
	proto.RegisterType((*PhenotypeAssociation)(nil), "bmeg.PhenotypeAssociation")
	proto.RegisterType((*Phenotype)(nil), "bmeg.Phenotype")
	proto.RegisterType((*GeneOntologyTerm)(nil), "bmeg.GeneOntologyTerm")
	proto.RegisterType((*Evidence)(nil), "bmeg.Evidence")
	proto.RegisterType((*Compound)(nil), "bmeg.Compound")
	proto.RegisterType((*DoseResponse)(nil), "bmeg.DoseResponse")
	proto.RegisterType((*ResponseSummary)(nil), "bmeg.ResponseSummary")
	proto.RegisterType((*ResponseCurve)(nil), "bmeg.ResponseCurve")
	proto.RegisterEnum("bmeg.ResponseSummary_SummaryType", ResponseSummary_SummaryType_name, ResponseSummary_SummaryType_value)
	proto.RegisterEnum("bmeg.ResponseCurve_ResponseType", ResponseCurve_ResponseType_name, ResponseCurve_ResponseType_value)
}

func init() { proto.RegisterFile("phenotype.proto", fileDescriptor6) }

var fileDescriptor6 = []byte{
	// 726 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x9c, 0x54, 0xcd, 0x6e, 0xda, 0x4a,
	0x14, 0xbe, 0x03, 0x06, 0xcc, 0x31, 0x21, 0x8e, 0x93, 0x7b, 0x35, 0xba, 0x2b, 0xea, 0x45, 0x14,
	0xa9, 0x12, 0x8d, 0x52, 0x51, 0x55, 0xdd, 0x21, 0x82, 0x28, 0x6a, 0x93, 0x54, 0x84, 0x34, 0xed,
	0x0a, 0x0d, 0x78, 0x80, 0x51, 0xec, 0x19, 0x6b, 0x66, 0x48, 0x83, 0xd4, 0xc7, 0xe8, 0x9b, 0xf4,
	0x11, 0xfa, 0x08, 0x7d, 0x9a, 0xee, 0xaa, 0x19, 0xdb, 0x24, 0x54, 0x5d, 0xa4, 0x5d, 0x71, 0xce,
	0xf8, 0xfc, 0x7c, 0xe7, 0xfb, 0xce, 0x01, 0x76, 0xd3, 0x25, 0xe5, 0x42, 0xaf, 0x53, 0xda, 0x4e,
	0xa5, 0xd0, 0x22, 0x70, 0xa6, 0x09, 0x5d, 0x84, 0x9f, 0xe1, 0xe0, 0x5d, 0xf1, 0xa1, 0xab, 0x94,
	0x98, 0x31, 0xa2, 0x99, 0xe0, 0x01, 0x40, 0x89, 0x45, 0x18, 0xb5, 0xd0, 0x51, 0x3d, 0xf0, 0xa0,
	0xbc, 0x60, 0x11, 0x2e, 0x59, 0xa7, 0x01, 0x8e, 0x89, 0xc5, 0x65, 0xeb, 0xed, 0x83, 0xb7, 0x24,
	0x6a, 0x90, 0x17, 0xc0, 0x4e, 0xab, 0x7c, 0x54, 0x0f, 0x0e, 0xa0, 0xb1, 0x24, 0x6a, 0x53, 0x16,
	0x57, 0xec, 0x6b, 0x00, 0xb0, 0x24, 0xaa, 0x27, 0xb8, 0xa6, 0x77, 0x1a, 0x57, 0xcd, 0x5b, 0x78,
	0x0d, 0xf5, 0x4d, 0xd8, 0x63, 0x5b, 0x36, 0xa1, 0xca, 0xd4, 0xf8, 0xbe, 0xdb, 0x3e, 0x78, 0x11,
	0x55, 0x33, 0xc9, 0x52, 0x03, 0x1c, 0x57, 0x4c, 0x50, 0xf8, 0x0d, 0x81, 0x3f, 0xa0, 0x9c, 0x5e,
	0x70, 0x2d, 0x62, 0xb1, 0x58, 0x8f, 0xa9, 0x4c, 0xb6, 0x1a, 0xec, 0x41, 0x9d, 0x93, 0x84, 0xaa,
	0x94, 0xcc, 0x68, 0xde, 0xc6, 0x83, 0x72, 0x44, 0xe7, 0x79, 0x97, 0x5d, 0xa8, 0xcd, 0x44, 0x92,
	0x50, 0xae, 0xb1, 0x53, 0x3c, 0xa8, 0x35, 0x17, 0x7c, 0x9d, 0x64, 0x2d, 0x0c, 0x2a, 0xa6, 0x26,
	0x24, 0x9b, 0xc4, 0xa0, 0x22, 0xb1, 0x9e, 0xb0, 0x08, 0xd7, 0x0a, 0x5f, 0xad, 0xa6, 0x8a, 0x6a,
	0xec, 0x5a, 0xbf, 0x01, 0xce, 0x9d, 0xa4, 0x73, 0x5c, 0x2f, 0x30, 0x33, 0x35, 0x11, 0x53, 0x25,
	0x62, 0xaa, 0x29, 0x86, 0x16, 0x3a, 0x72, 0x03, 0x1f, 0xdc, 0x99, 0xe0, 0x8a, 0x45, 0x54, 0x62,
	0xcf, 0xd2, 0xf3, 0x05, 0x81, 0xdb, 0xbf, 0x65, 0x11, 0xe5, 0xb3, 0x47, 0xd3, 0xd3, 0x00, 0x27,
	0x4d, 0x58, 0x94, 0x93, 0x73, 0x08, 0x0e, 0xe3, 0x73, 0x61, 0x25, 0xf0, 0x4e, 0x70, 0xdb, 0x68,
	0xde, 0x2e, 0x4a, 0xb6, 0x87, 0x7c, 0x2e, 0xfa, 0x5c, 0xcb, 0xf5, 0xff, 0x4f, 0xa1, 0xbe, 0x71,
	0x4c, 0xf5, 0x1b, 0xba, 0xce, 0x5b, 0xed, 0x40, 0xe5, 0x96, 0xc4, 0xab, 0x9c, 0xa4, 0x57, 0xa5,
	0x97, 0x28, 0xfc, 0x81, 0xc0, 0xed, 0x89, 0x24, 0x15, 0x2b, 0x1e, 0xfd, 0x01, 0x2c, 0xc3, 0x77,
	0x4e, 0xa6, 0x61, 0x27, 0x61, 0x31, 0x55, 0xb8, 0x5e, 0xf8, 0x9a, 0xc8, 0x05, 0xd5, 0x39, 0xb7,
	0x4d, 0xa8, 0x4a, 0x9a, 0x0a, 0x69, 0xf6, 0xa4, 0x88, 0xd7, 0x44, 0xaf, 0x14, 0xae, 0x15, 0xea,
	0x49, 0xbb, 0xa7, 0x24, 0xa6, 0xd8, 0xb5, 0x4f, 0x3e, 0xb8, 0xb9, 0x3e, 0x0a, 0xc3, 0xd6, 0xec,
	0xde, 0xc3, 0xd9, 0x0b, 0xdc, 0x7f, 0x3b, 0x7b, 0x1b, 0x1a, 0xa7, 0x42, 0xd1, 0x11, 0x55, 0xa9,
	0xe0, 0x8a, 0x9a, 0xb9, 0x22, 0xa1, 0xa8, 0x4d, 0x40, 0x06, 0x84, 0xcc, 0xbf, 0xd8, 0x1c, 0x14,
	0x7e, 0x47, 0xb0, 0x5b, 0x04, 0x5f, 0xae, 0x92, 0x84, 0xc8, 0x75, 0xf0, 0x2c, 0x67, 0xc6, 0xe4,
	0x34, 0x4f, 0x9e, 0x64, 0xc0, 0x7e, 0x09, 0x6a, 0xe7, 0xbf, 0x66, 0xd1, 0xb7, 0x71, 0x20, 0xd3,
	0x73, 0xc5, 0x99, 0xce, 0x98, 0x0d, 0x25, 0x78, 0x0f, 0x63, 0x3d, 0xa8, 0x5d, 0x9d, 0xbf, 0x39,
	0xbf, 0xb8, 0x3e, 0xf7, 0xff, 0x09, 0x5c, 0x70, 0xfa, 0xbd, 0xce, 0xb1, 0x8f, 0x8c, 0x35, 0x34,
	0x56, 0xc9, 0x58, 0x6f, 0x4f, 0x3b, 0xc7, 0x7e, 0xd9, 0x58, 0x83, 0x51, 0xe7, 0xd8, 0x77, 0x8c,
	0xd5, 0x3d, 0xeb, 0x7e, 0xf0, 0x2b, 0x41, 0x0d, 0xca, 0xdd, 0xab, 0x9e, 0x5f, 0x0d, 0xf6, 0x60,
	0xa7, 0xdb, 0x1b, 0x0f, 0xdf, 0x0f, 0xc7, 0x1f, 0x27, 0xdd, 0x51, 0xbf, 0xeb, 0xd7, 0x4c, 0xd4,
	0xe8, 0xec, 0xb2, 0xef, 0xbb, 0xe1, 0xd7, 0x12, 0xec, 0x14, 0x80, 0x7b, 0x2b, 0x79, 0x4b, 0x0b,
	0xe9, 0x33, 0xde, 0x5e, 0x40, 0xa3, 0xa0, 0xc1, 0x1e, 0x6a, 0xc9, 0x0e, 0xda, 0xda, 0x1e, 0xd4,
	0xe6, 0x6d, 0x3c, 0x8b, 0x3d, 0x84, 0xaa, 0x9d, 0x53, 0xe1, 0xb2, 0xd5, 0x2c, 0xc8, 0x32, 0xb6,
	0x08, 0xff, 0x0f, 0x9a, 0x0b, 0x29, 0x3e, 0xe9, 0xe5, 0xa5, 0x26, 0x3c, 0x22, 0x32, 0xb2, 0x2b,
	0x85, 0xb2, 0xeb, 0xc9, 0xb4, 0xbd, 0x5f, 0x22, 0x45, 0x92, 0x34, 0xa6, 0xf9, 0x12, 0x1d, 0x42,
	0x4d, 0x65, 0x44, 0xd9, 0x1b, 0xf5, 0x4e, 0xfe, 0xfd, 0x2d, 0xf3, 0xf9, 0x1d, 0x6a, 0x29, 0x62,
	0x65, 0x8f, 0x17, 0x99, 0x4a, 0xd3, 0x98, 0xf0, 0x1b, 0x65, 0xcf, 0x17, 0x85, 0x1d, 0x68, 0x6c,
	0xe1, 0xde, 0xe2, 0x1c, 0xa0, 0x3a, 0x18, 0x5d, 0x5c, 0x8f, 0x5f, 0xfb, 0x46, 0x29, 0xb7, 0x20,
	0xd1, 0x2f, 0x4d, 0xab, 0xf6, 0x8f, 0xf7, 0xf9, 0xcf, 0x00, 0x00, 0x00, 0xff, 0xff, 0xb8, 0x8b,
	0xdf, 0x76, 0x8b, 0x05, 0x00, 0x00,
}
